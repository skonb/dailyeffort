import sys
import datetime
import re


# シフト調査票の形式を守っているか，すでに調査票が提出されているかを判定する
# 形式が守られている場合，人手が足りていない時間帯にシフトを追加する
# 8時間を超えないように早い時間から優先して加えていく
# 識別ID，出勤可能機関の数,勤務シフト表，すでにシフトを提出した人の識別IDset
def submit(X, S, workable_days, worktime_list, submitted, K):
    if X in submitted:
        for m in worktime_list:
            for d in m:
                for h in d:
                    for assigned_person in h:
                        assigned_person.discard(X)

    else:
        submitted.add(X)
    # datetimeはMM/DD hh:mm-hh-mmの形式で表される
    #('01', '31', '09', '00', '12', '00')
    for schedule in workable_days:
        month, date, hour1, minute1, hour2, minute2 = map(int, schedule)
        # print(schedule)
        # 一日ごとに勤務時間を計測，，8時間=480分を超えたらその日はシフトを追加しない
        tmp_worktime = 0
        for append_target in [worktime_list[month][date][hour1][minute1:], worktime_list[month][date][hour1+1:hour2], worktime_list[month][date][hour2][:minute2+1]]:
            for assigned_person in append_target:
                if len(assigned_person) < K:
                    assigned_person.add(X)
                    if tmp_worktime >= 480:
                        break
                    tmp_worktime += 1
    print('accepted')


def check(X, worktime_list):
    workday = []
    for MM, m in enumerate(worktime_list):
        for DD, d in enumerate(m):
            breakFlag = False
            for h in d:
                for assigned_person in h:
                    if X in assigned_person:
                        workday.append(f'{MM:02}/{DD:02}')
                        breakFlag = True
                    break
                if breakFlag:
                    break
    print(len(workday))
    print(' '.join(workday))
# 分給は900/60=15
# 深夜割増手当なら900*1.2/60=18


def calculate(X, worktime_list):
    paying = 0
    work_minute = 0
    for m in worktime_list:
        for d in m:
            for hour, h in enumerate(d):
                for assigned_person in h:
                    if X in assigned_person:
                        # ここの範囲は設問を見ないとわからない
                        paying += 15 if hour > 4 and hour < 22 else 18
                        work_minute += 1
    # 40時間=2400分以上？
    if work_minute >= 2400:
        paying += 10000
    print(paying)
    print(work_minute)


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    # for i, v in enumerate(lines):
    #    print("line[{0}]: {1}".format(i, v))
    lines_iter = iter(lines)
    A, B, D, K, T = map(int, next(lines_iter).split())
    worktime_list = [[[[set() for _ in range(1, 59+1)] for _ in range(1, 23+1)]
                      for _ in range(1, 31+1)] for _ in range(A, 12+1)]
    submitted = set()
    for _ in range(T):
        query = next(lines_iter)
        if query == 'submit':
            X = next(lines_iter)
            S = next(lines_iter)
            workable_days = re.findall(
                r'(\d+)\/(\d+) (\d+):(\d+)-(\d+):(\d+)', next(lines_iter))
            # print(workable_days)
            submit(X, S, workable_days, worktime_list, submitted, K)
        elif query == 'cancel':
            pass
        elif query == 'check':
            X = next(lines_iter)
            check(X, worktime_list)
        else:  # T==calculate
            X = next(lines_iter)
            calculate(X, worktime_list)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
