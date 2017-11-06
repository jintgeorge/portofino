from flask_restful import Resource

class GetLog(Resource):
    def get(self):
        count = {}
        with open('request_log.log') as f:
            lines = f.readlines()
            for line in lines:
                t = line.split('|')
                ip = t[0].strip()
                endpoint = t[1].strip()
                timestamp = t[2].strip()
                print(ip)

                if ip not in count:
                    count[ip] = {}
                if endpoint not in count[ip]:
                    count[ip][endpoint] = []
                count[ip][endpoint].append(timestamp)
        print(count)
        return count