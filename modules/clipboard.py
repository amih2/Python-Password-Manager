import subprocess

class ClipBoard:

    def get_dlipboard_data(self):
        p = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
        retcode = p.wait()
        data = p.stdout.read()
        return data

    def set_clipboard_data(self, data):
        p = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
        p.stdin.write(data)
        p.stdin.close()
        retcode = p.wait()
