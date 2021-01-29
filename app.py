import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import requests 
import urllib.request

################ DEF TO INPUT VIDEO ID AND OUTPUT RESPONSE CODE AND VIEW COUNT
 
def  YT_API_pull(video_id):
  # open a connection to a URL using urllib
  webUrl ='https://www.googleapis.com/youtube/v3/videos?key=AIzaSyBInsFf7pyAxa1qEffe9CrSGNOcueNCqmw&fields=items(statistics(viewCount))&part=snippet,statistics&id=' + video_id 
  webUrl  = urllib.request.urlopen(webUrl)
 
  #get the result code and print it
  #print ("result code: " + str(webUrl.getcode()))
  rep_code = webUrl.getcode()
 
  # read the data from the URL and print it
  data = webUrl.read()
  #print (data)
 
  data = data.decode("utf-8")
 
  #By brute force, view count number in the response will start position: pos(viewCount) + 13
  result = data.find('viewCount') 
  #print ("Substring 'viewCount ' found at index:", result ) 
 
  #output number
  num = ''
  i = result + 13
  while(data[i] != '"'):
    num = num + data[i]
    i += 1
 
  num = int(num)
 
 
  return rep_code, num

########## lect number and view count array
 
lect_no = ['V0', 'V1', 'V2 P1', 'V2 P2', 'V3 P1', 'V3 P2', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 
'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25']

view_ct = [YT_API_pull(video_id = 'Bo7iVSs5z6s')[1], YT_API_pull(video_id = 'hYdZjXceBYg')[1], YT_API_pull(video_id = '3w-_NqFJW30')[1],
YT_API_pull(video_id = 'JYhUh_YYY9s')[1], YT_API_pull(video_id = 'uP7AI6rha9E')[1], YT_API_pull(video_id = 's_gEqgBbw9k')[1], 
YT_API_pull(video_id = 'iWEh8bqvseE')[1], YT_API_pull(video_id = '37RlofthNdM')[1], YT_API_pull(video_id = 'Phu6sGsK0g8')[1], 
YT_API_pull(video_id = 'iWrB-rhGAoo')[1], YT_API_pull(video_id = 'tuRYYn7ncZM')[1], YT_API_pull(video_id = 'zn18jg3B_CA')[1], 
YT_API_pull(video_id = 'bFMoUeXpFVg')[1], YT_API_pull(video_id = 'UK8BMltgpFI')[1], YT_API_pull(video_id = 'Ci_neJGO0gY')[1], 
YT_API_pull(video_id = 'rZbxPjyKbzE')[1], YT_API_pull(video_id = '504U7TOHSwA')[1], YT_API_pull(video_id = '0lIkg6AibMs')[1], 
YT_API_pull(video_id = '6DpoONQCt9g')[1], YT_API_pull(video_id = '_kmAOOWq4U8')[1], YT_API_pull(video_id = 'PKoQNxlTFnY')[1],
YT_API_pull(video_id = 'cxp_uGBDcaU')[1], YT_API_pull(video_id = 'ONFw_-NF1jg')[1], YT_API_pull(video_id = 'HQBmqCZyRUI')[1],
YT_API_pull(video_id = 'Siruz9slidg')[1], YT_API_pull(video_id = 'VA-e46Ze2ZE')[1], YT_API_pull(video_id = 'FdKyOyYpWHI')[1],
YT_API_pull(video_id = '1K0HZj0Yyhw')[1]]


# Generate the figure dictionary
#fig = go.Figure(data=data,layout=layout)
fig = go.Figure([go.Bar(x=lect_no, y = view_ct)])
########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
