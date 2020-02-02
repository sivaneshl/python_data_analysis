import numpy as np
import pandas as pd

def blight_model():
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import roc_auc_score
    from sklearn.model_selection import train_test_split

    train_data = pd.read_csv('../resources/train.csv', encoding='ISO-8859-1')
    train_data = train_data[pd.notnull(train_data['compliance'])]
    train_data.set_index('ticket_id', inplace=True)

    test_data = pd.read_csv('../resources/test.csv', encoding='ISO-8859-1')
    test_data.set_index('ticket_id', inplace=True)

    addresses = pd.read_csv('../resources/addresses.csv')
    latlons = pd.read_csv('../resources/latlons.csv')

    pd.merge(addresses, latlons, on='address', how='left')
    pd.merge(train_data, addresses, on='ticket_id', how='left')
    pd.merge(test_data, addresses, on='ticket_id', how='left')

    leakage_columns = ['payment_amount', 'payment_date', 'payment_status', 'balance_due', 'collection_status',
                      'compliance', 'compliance_detail']
    remove_columns = ['agency_name', 'inspector_name', 'violator_name', 'violation_street_number',
                      'violation_street_name', 'violation_zip_code', 'mailing_address_str_number', 'disposition',
                      'mailing_address_str_name', 'city', 'state', 'zip_code', 'non_us_str_code', 'grafitti_status',
                      'country', 'ticket_issued_date', 'hearing_date', 'violation_code', 'violation_description']

    y_train = train_data['compliance']
    X_train = train_data.drop(leakage_columns+remove_columns, axis=1)
    X_test = test_data.drop(remove_columns, axis=1)

    clf = RandomForestClassifier(n_estimators=100, n_jobs=-1, max_depth=10, random_state=0).fit(X_train, y_train)
    test_data['compliance'] = clf.predict_proba(X_test)[:,1]

    X_train_1, X_test_1, y_train_1, y_test_1 = train_test_split(X_train, y_train)
    print(roc_auc_score(y_test_1, clf.predict_proba(X_test_1)[:,1]))
    print(X_train.columns.to_list())

    return test_data['compliance']


print(blight_model())