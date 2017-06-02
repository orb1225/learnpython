import sys
import subprocess
from threading import Timer

class MaxellUtile(object):
    '''
    Tool For Maxell
    '''

    @staticmethod
    def command(cmd, timeout=0):
        '''
        System call执行系统命令，并返回执行结果和消息
        '''

        p=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if timeout > 0:
            kill_proc = lambda p: p.kill()
            timer = Timer(timeout, kill_proc, [p])
            try:
                timer.start()
                retval=p.wait()
            finally:
                timer.cancel()
        else:
            retval=p.wait()

        outmsg = ''.join(p.stdout.readlines())
        errmsg = ''.join(p.stderr.readlines())
        return retval, outmsg, errmsg

    @staticmethod
    def exec_command(cmd, timeout=0):
        '''
        System call执行系统命令，并返回执行结果和消息
        '''
        retval, outmsg, errmsg = MaxellUtile.command(cmd, timeout)

        print(outmsg, errmsg)
        return retval,outmsg

    @staticmethod
    def exec_hive_command(cmd, timeout=0):
        '''
        System call执行系统命令，并返回执行结果和消息
        '''
        retval, outmsg, errmsg = MaxellUtile.command(cmd, timeout)
        for row in errmsg.split("\n"):
            if "Kill Command = " in row:
                new_command = row.replace("Kill Command = ", "")
                MaxellUtile.command(new_command, 0)

        print(outmsg, errmsg)
        return retval,errmsg

SAFE_COMMAND = MaxellUtile.exec_command
ret, msg = SAFE_COMMAND("ps -ef")
print(ret,msg)