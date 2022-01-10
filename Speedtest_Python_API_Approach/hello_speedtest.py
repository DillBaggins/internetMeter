import speedtest

s=None
threads=None

def ooklaInit():
    global s
    servers = []
    # If you want to test against a specific server
    # servers = [1234]

    # If you want to use a single threaded test
    # threads = 1

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()

def ooklaTest():
    global s,threads
    s.download(threads=threads)
    results_dict = s.results.dict()
    return (results_dict["download"]/(10**6))

    