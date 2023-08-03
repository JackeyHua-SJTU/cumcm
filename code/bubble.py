import plotly.graph_objects as go

# define the size of bubbles
size = [20, 40, 60, 80, 100, 80, 60, 40, 20, 40]
fig = go.Figure(data=[go.Scatter(
    # x-coordinate of the center of the bubble
    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    # y-coordinate of the center of the bubble
    y=[11, 12, 10, 11, 12, 11, 12, 13, 12, 11],
    mode='markers',
    marker=dict(
        size=size,
        # set the RGB color
        color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',
               'rgb(44, 160, 101)', 'rgb(255, 65, 54)',
               'rgb(207, 114, 255)', 'rgb(127, 96, 0)',
               'rgb(255, 140, 184)', 'rgb(79, 90, 117)',
               'rgb(222, 223, 0)', 'rgb(150, 193, 0)'],
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4
    )
)])

fig.update_layout(title='Bubble Chart Demo',
                  xaxis=dict(
                      title='demo x-axis',
                      gridcolor='white',
                      # log-based axis
                      type='log',
                      gridwidth=2,
                  ),
                  yaxis=dict(
                      title='demo y-axis',
                      gridcolor='white',
                      gridwidth=2,
                  ),
                  paper_bgcolor='rgb(243, 243, 243)',
                  plot_bgcolor='rgb(243, 243, 243)',
                  )

fig.show()
