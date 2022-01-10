import speedtest

servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()

for i in range(1):
    s.download(threads=threads)
    results_dict = s.results.dict()
    print(results_dict["download"]/(10**6))

results_dict = s.results.dict()

print(results_dict)