from anticaptchaofficial.hcaptchaproxyless import hCaptchaProxyless
import requests
import json
import time 
import threading

"""
https://github.com/AdminAnticaptcha/anticaptcha-python - anti-captcha com api doc
"""


class dvachdesc():
    """
    2ch api descriptor class
    """
    def __init__(self, anticaptcha_key, gb=True):
        """
        anticaptcha_key - str  | anti-captcha com api key
        gb              - bool | True default | Show blance on startup
        """
        self.solver = hCaptchaProxyless()
        self.solver.set_key(anticaptcha_key)
        self.solver.set_website_url("https://2ch.hk/")
        # self.solver.set_website_url("https://2ch.pm/")
        # self.solver.set_verbose(1) # debug
        self.solver.set_website_key("248cebfd-9b3f-4d8c-88b5-f812daf51261") # 2ch google captcha site key

        if gb:
            self.get_balance()

    def get_balance(self):
        print("Balance: {} $".format(self.solver.get_balance()))

    def send_post(self, board, thread, comment, filepath=None, email=''):
        """
        board    - int | b/vg/v/s/etc
        thread   - int | thread's number
        comment  - str | post's text
        filepath - str | path to image
        email    - str | post's email field. set to 'sage' as optional
        """
        if filepath:
            file = {}
            file['image'] = open(filepath,'rb').read()
        else:
            file = None

        g_response = self.solver.solve_and_return_solution()
        if g_response != 0:
            req = requests.post("https://2ch.hk/makaba/posting.fcgi?json=1", data={
                'task':'post',
                'board': board,
                'thread': thread,
                'captcha_type':'hcaptcha',
                '2chaptcha_id': '248cebfd-9b3f-4d8c-88b5-f812daf51261',
                'email': email,
                'comment': comment,
                'h-captcha-response': g_response
                
                },files = file if file is not None else {'img': None} ).text
            
            req = json.loads(req)
            
            if req['Error'] == None:
                print( "{} {} Post {} sent".format(req["Status"], time.strftime("%X"), req["Num"]) )
                return req["Num"]
            else:
                print("Err {} {}".format(time.strftime("%X"), req))
                return 0
        else:
            print("task finished with error " + self.solver.error_code)
            return 0

    def send_multi_posts(self, board, thread, comment, tasks, delay=15):
        """
        board   - int | b/vg/v/s
        thread  - int | thread number
        comment - str | post text
        tasks   - int | posts' quantity
        delay   - int | posts' delay
        """
        threads = []

        for i in range(tasks):
            task = threading.Thread(target=self.send_post, args=(board, thread, comment,))
            threads.append(task)
   
        for i in threads:
            i.run()
            time.sleep(delay)

