import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# crete a twin plot
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
plt.title('Who is the most successful and consistent team In IPL 2008-2019?\n'
          'Chennai Super Kings (CSK) vs. Mumbai Indians (MI) vs. Kolkata Knight Riders (KKR)')


# function definitions
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
        ax2.text(bar.get_x() + bar.get_width() / 2,
                 bar.get_height()-0.5,
                 str(10 - int(bar.get_height())),
                 ha='center', color='black', fontsize=11)


# constants
year_list = list(range(2008, 2019))
team_list = ['csk', 'mi', 'kkr']
team_color = dict(zip(team_list, ['yellow', 'blue', 'purple']))
team_bar_pos = dict(zip(team_list, list(np.arange(-.2, .3, .2))))
team_df_dict = {}
champion_df_dict = {}

# read data
for team in team_list:
    team_df_dict[team] = pd.read_csv('data/'+team+'_data.csv',
                                     usecols=['Year', 'Total', 'Wins', 'Losses', 'Position'],
                                     index_col='Year')

# cleanup activity
team_df_dict['csk']['Position'] = team_df_dict['csk']['Position'].replace(r'[a-z]', '', regex=True).astype(int)
team_df_dict['mi']['Position'] = team_df_dict['mi']['Position'].replace('Champion', 1).astype(int)
team_df_dict['kkr']['Position'] = team_df_dict['kkr']['Position'].apply(lambda x: x.split('/')[0]).astype(int)

for team in team_list:
    # compute win %
    win_pct(team_df_dict[team])
    # get champions of the year
    champion_df_dict[team] = champion_years(team_df_dict[team])
    # plot win % -  line graph
    plot_win_pct(team_df_dict[team].index.values,
                 team_df_dict[team]['Win%'],
                 team_color[team], team.upper())
    # plot champion of the year - scatter points
    plot_champions(champion_df_dict[team].index.values,
                   champion_df_dict[team]['Win%'],
                   team_color[team], team.upper())
    # plot finish position - bar chart
    plot_position(team_df_dict[team].index.values + team_bar_pos[team],
                  team_df_dict[team]['Position'],
                  team_color[team], team.upper())

# benchmark line for win %
ax1.axhline(y=55, color='k', linewidth=2, linestyle='--')
ax1.text(2019.65, 55, 'Benchmark=55%', bbox=dict(fc='white', ec='k'))

# axes labels and formatting
plt.xticks(year_list, year_list)
ax1.set_xlabel('Year')
ax1.set_ylabel('Win%')
ax2.tick_params(right=False)
ax2.set_yticklabels([])

# legend work
legend1, legend_labels1 = ax1.get_legend_handles_labels()
legend2, legend_labels2 = ax2.get_legend_handles_labels()
plt.legend(legend1+legend2, legend_labels1+legend_labels2,
           loc='lower center', ncol=3, title='Legend', frameon=1, facecolor='white', framealpha=1, fancybox=True)

# footnote
plt.figtext(0.99, 0.01, 'Note: Plot colors are selected based on team jersy colors',
            horizontalalignment='right', color='grey', fontsize='small', fontstyle='italic')

mng = plt.get_current_fig_manager()
mng.window.state('zoomed')

# plt.savefig('assignment4.1.png')
plt.show()
