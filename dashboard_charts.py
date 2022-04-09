import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import ConnectionPatch


def students_by_cgpa(df2):
    plt.figure(figsize=(10,10))
    sizes = df2["CGPA"].value_counts().tolist()
    labels = df2["CGPA"].value_counts().index.tolist()
    
    colors = ['#FF0000', '#0000FF', '#FFFF00', '#ADFF2F', '#FFA500', '#FFA700']
    
    explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
    
    centre_circle = plt.Circle((5, 5), 0.70, fc='white')
    fig, axs = plt.subplots(2, 1, constrained_layout=True)
    
    fig = plt.gcf()

    fig.gca().add_artist(centre_circle)
    
    axs[0].set_title('Students by CGPA')
    
    # Pie Chart
    axs[0].pie(sizes, colors=colors, labels=labels, textprops={'fontsize': 8},
            autopct='%1.1f%%', pctdistance=0.75, 
            explode=explode)
    
    cross_tab_Q1_group = pd.crosstab([df2.ModuleTitle], [df2.CGPA])

    cross_tab_Q1_group.plot(kind="barh", stacked=True, color=[
        sns.xkcd_rgb["crimson"],
        sns.xkcd_rgb["burnt orange"],
        sns.xkcd_rgb["denim blue"],
        sns.xkcd_rgb["turquoise"],
        sns.xkcd_rgb["spring green"], 
        sns.xkcd_rgb['medium green'], 
    ], ax=(axs[1]))
    
    
    axs[1].set_ylabel('ModuleTitle')
    axs[1].set_title('Rating of students by CGPA and modules')

    plt.show()

    return fig

def students_by_attention(df2):
    plt.figure(figsize=(10,10))
    fig, axs = plt.subplots(1, 1, constrained_layout=True)

    axs.set_ylabel('ModuleTitle')
    axs.set_title('Rating of students by attention on courses videos')

    cross_tab_Q2_group = df2.groupby(by=['ModuleTitle'])['Played','Paused','Segment'].sum()
    cross_tab_Q2_group.plot(kind="barh", stacked=True, color=[
        sns.xkcd_rgb["crimson"],
        sns.xkcd_rgb["burnt orange"],
        sns.xkcd_rgb["denim blue"],
        sns.xkcd_rgb["turquoise"],
        sns.xkcd_rgb["spring green"], 
        sns.xkcd_rgb['medium green'], 
    ], ax=(axs))

    return fig

def students_by_attempts(df2):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
    fig.subplots_adjust(wspace=0)
    # pie chart parameters
    df3 = df2.groupby(by=['Result'])['AttemptCount'].value_counts()
    passed_share = df3.Pass.sum() / df3.sum()
    failed_share = df3.Fail.sum() / df3.sum()
    overall_ratios = [
        failed_share,
        passed_share,
    ]
    labels = ['Fail', 'Pass']
    explode = [0, 0.1]

    angle = -180 * overall_ratios[0]
    wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                        labels=labels, explode=explode)

    df3 = df2.groupby(by=['Result'])['AttemptCount'].value_counts()
    df3_dict = df3.Fail.to_dict()
    attempts = list(df3_dict.values())

    attempt_labels = df3_dict.keys()
    bottom = 1
    width = .2

    for j, (height, label) in enumerate(reversed([*zip(attempts, attempt_labels)])):
        bottom -= height / 100
        bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label,
                    alpha=0.1 + 0.25 * j)
        ax2.bar_label(bc, labels=[height], label_type='center', fontsize=8)

        ax2.set_title('Students by number of attempts')
        ax2.legend()
        ax2.axis('off')
        ax2.set_xlim(- 2.5 * width, 2.5 * width)

        theta1, theta2 = wedges[0].theta1, wedges[0].theta2
        center, r = wedges[0].center, wedges[0].r
        bar_height = sum(attempts) / 100

        x = r * np.cos(np.pi / 180 * theta2) + center[0]
        y = r * np.sin(np.pi / 180 * theta2) + center[1]
        con = ConnectionPatch(xyA=(-width / 2, bar_height*93), coordsA=ax2.transData,
                            xyB=(x, y), coordsB=ax1.transData)
        con.set_color([0, 0, 0])
        con.set_linewidth(4)
        ax2.add_artist(con)

        x = r * np.cos(np.pi / 180 * theta1) + center[0]
        y = r * np.sin(np.pi / 180 * theta1) + center[1]
        con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                            xyB=(x, y), coordsB=ax1.transData)
        con.set_color([0, 0, 0])
        ax2.add_artist(con)
        con.set_linewidth(4)

    return fig
