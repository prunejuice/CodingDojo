call_list = []
class Call(object):


    def __init__(self, unique_id, caller_name, caller_number, time_call, call_reason):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.time_call = time_call
        self.call_reason = call_reason

    def display(self):
        print self.unique_id
        print self.caller_name
        print self.caller_number
        print self.time_call
        print self.call_reason


class CallCenter(object):
    def __init__(self, calls):
        self.calls = calls
        self.queue_size = len(calls)

    def add(self, call):
        call_list.append(call)

    def remove():
        del call_list[0]

    def info(self):

        length = len(call_list)
        for i in range(0, length):
            print call_list[i].caller_name
            print call_list[i].caller_number
        print "test"


caller1 = Call(1, "Jonathan", 911, "12PM", "Complaint")
caller2 = Call(2, "Jim", 211, "13PM", "Feedback")

call_list.append(caller1)
call_list.append(caller2)
telstra = CallCenter(call_list)

telstra.info()
