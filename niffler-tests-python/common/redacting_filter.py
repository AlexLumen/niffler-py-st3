import logging


class RedactingFilter(logging.Filter):
    def __init__(self, patterns: list):
        super().__init__()
        self._patterns = patterns

    def filter(self, record):
        record.msg = self.redact(record.msg)
        # if isinstance(record.args, dict):
        #     for key in record.args.keys():
        #         record.args[key] = self.redact(record.args[key])
        # else:
        #     record.args = tuple(self.redact(arg) for arg in record.args)
        record.args = tuple(self.redact(arg) for arg in record.args)
        return True

    def redact(self, msg: str):
        msg = isinstance(msg, str) and msg or str(msg)
        for pattern in self._patterns:
            msg = msg.replace(pattern, '******')
        return msg
