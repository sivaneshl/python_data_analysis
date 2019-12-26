import pandas as pd
import matplotlib.pyplot as plt

team_list = ['csk', 'mi', 'kkr']
team_color = dict(zip(team_list, ['yellow', 'blue', 'purple']))
team_label = dict(zip(team_list, ['CSK', 'MI', 'KKR']))

csk_df = pd.read_csv('data/csk_data.csv',
                     usecols=['Year', 'Total', 'Wins', 'Losses', 'Position'],
                     index_col='Year')
mi_df = pd.read_csv('data/mi_data.csv',
                    usecols=['Year', 'Total', 'Wins', 'Losses', 'Position'],
                    index_col='Year')
kkr_df = pd.read_csv('data/kkr_data.csv',
                     usecols=['Year', 'Played', 'Wins', 'Losses', 'Position'],
                     index_col='Year')


# cleanup
csk_df['Position'] = csk_df['Position'].replace(r'[a-z]', '', regex=True).astype(int)
mi_df['Position'] = mi_df['Position'].replace('Champion',1).astype(int)
kkr_df.rename(columns={'Played':'Total'}, inplace=True)
kkr_df['Position'] = kkr_df['Position'].apply(lambda x: x.split('/')[0]).astype(int)

# team_size = dict(zip(list(range(2008, 2019)), [8, 8, 8, 10, 9, 9, 8, 8, 8, 8, 8, 8]))
# team_size = pd.DataFrame({'nbr_of_teams':[8,8,8,10,9,9,8,8,8,8,8,8]}, index=np.arange(2008, 2020))


def win_pct(df):
    df['Win%'] = df['Wins'] / (df['Wins'] + df['Losses']) * 100


def champion_years(df):
    return df[df['Position'] == 1]


def plot_win_pct(x, y, c, l):
    ax1.plot(x, y, color=c, label=l + ' Win%')


def plot_champions(x, y, c, l):
    ax1.scatter(x=x, y=y, c=c, s=20, marker='o', label=l + ' - Champions')


def plot_position(x, y, c, l):
    bars = ax2.bar(x, 10-y, alpha=0.2, width=0.2, color=c, label=l + ' - Position')
    for bar in bars:
        ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height()-0.5, str(10 - int(bar.get_height())),
                 ha='center', color='black', fontsize=11)


win_pct(csk_df)
win_pct(mi_df)
win_pct(kkr_df)

csk_champions = champion_years(csk_df)
mi_champions = champion_years(mi_df)
kkr_champions = champion_years(kkr_df)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

plot_win_pct(csk_df.index.values, csk_df['Win%'], team_color['csk'], team_label['csk'])
plot_win_pct(mi_df.index.values, mi_df['Win%'], team_color['mi'], team_label['mi'])
plot_win_pct(kkr_df.index.values, kkr_df['Win%'], team_color['kkr'], team_label['kkr'])

plot_champions(csk_champions.index.values, csk_champions['Win%'], team_color['csk'], team_label['csk'])
plot_champions(mi_champions.index.values, mi_champions['Win%'], team_color['mi'], team_label['mi'])
plot_champions(kkr_champions.index.values, kkr_champions['Win%'], team_color['kkr'], team_label['kkr'])

plot_position(csk_df.index.values-0.2, csk_df['Position'], team_color['csk'], team_label['csk'])
plot_position(mi_df.index.values, mi_df['Position'], team_color['mi'], team_label['mi'])
plot_position(kkr_df.index.values+0.2, kkr_df['Position'], team_color['kkr'], team_label['kkr'])

ax1.axhline(y=55, color='k', linewidth=2, linestyle='--')
ax1.text(2019.65, 55, 'Benchmark=55%', bbox=dict(fc='white', ec='k'))

plt.title('Who is the successful and consistent team In IPL 2008-2019?\n'
          'Chennai Super Kings (CSK) vs. Mumbai Indians (MI)')
plt.xticks(mi_df.index, mi_df.index.values)
ax1.set_xlabel('Year')
ax1.set_ylabel('Win%')
ax2.tick_params(right=False)
ax2.set_yticklabels([])

legend1, legend_labels1 = ax1.get_legend_handles_labels()
legend2, legend_labels2 = ax2.get_legend_handles_labels()
plt.legend(legend1+legend2, legend_labels1+legend_labels2,
           loc='lower center', ncol=3, title='Legend', frameon=1, facecolor='white', framealpha=1, fancybox=True)
plt.figtext(0.99, 0.01, 'Note: Plot colors are selected by team jersy colors',
            horizontalalignment='right', color='grey', fontsize='small', fontstyle='italic')

plt.show()
