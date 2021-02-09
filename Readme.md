# P2P File Sharing Application with Python

This is a p2p file sharing application developed with Python language using socket programming.

## Getting Started

Copy the Service_Listener, Service_Announcer,  P2P_Downloader,  P2P_Server files in a folder.

### Prerequisites

```
Download a file smaller than 100 kb and put it in your main folder which contains your python files.
```

### Installing

```
You need to have Python 3.8 and text editor if you want to see codes and update
```

## Running the tests

Let's say you have a file which is called "file.txt" in your folder.
1) Run P2P_Server and enter "file.txt" which is your filename.
2) Run Service_Announcer and enter any username you want.
3) Run Service_Listener and see the result. It will show you usernames , ip adresses,files and chunks in 60s periods.
4) Run P2P_Downloader , you can enter any file name you want but now lets say "file.txt". Then enter the ip adress of the server you want to connect. You can see the ip adress from Service_Listener. For now, you are the server of yours but if you connect with hamachi network with some people , you will see more servers on Service_Listener.



