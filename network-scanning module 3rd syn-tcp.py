from socket import *
import threading

lock = threading.Lock()
openNum = 0
threads = []

def portScanner(host,port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()
        openNum+=1
        print('[+] %d open' % port)
        lock.release()
        s.close()
    except:
        pass

def main():
    setdefaulttimeout(1)
    IP=raw_input('Input IP :')
    PORT=raw_input('Input PORT:')
    list = PORT.split(",")
    for i in range(len(list)):
        if list[i].isdigit():
            t = threading.Thread(target=portScanner, args=(IP, int(list[i])))
            threads.append(t)
            t.start()
        else:
            newlist = list[i].split("-")
            startPort = int(newlist[0])
            endPort = int(newlist[1])
            for p in range(startPort, endPort):
                t = threading.Thread(target=portScanner, args=(IP, p))
                threads.append(t)
                t.start()

    for t in threads:
        t.join()

    print('[*] The scan is complete!')
    print('[*] A total of %d open port ' % (openNum))

if __name__ == '__main__':
    main()