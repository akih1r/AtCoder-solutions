#ランレングス圧縮
def rle(xs):
    if not xs:
        return []
    res = []
    cur, cnt = xs[0], 1
    for x in xs[1:]:
        if x == cur:
            cnt += 1
        else:
            res.append((cur, cnt))
            cur, cnt = x, 1
    res.append((cur, cnt))
    return res


def un_rle(S_rle):
    result_blocks = []
    for k, v in S_rle:
        result_blocks.append(k * v)

    ans = "".join(result_blocks)
    return ans

#拡張版
def rle(xs, skip={"A", "B", "C"}):
    if skip is None:
        skip = set()
    elif not isinstance(skip, set):
        skip = {skip}
    if not xs:
        return []
    res = []
    cur, cnt = xs[0], 1
    for x in xs[1:]:
        if x == cur and x not in skip:
            cnt += 1
        else:
            res.append((cur, cnt))
            cur, cnt = x, 1
    res.append((cur, cnt))
    return res


#特定のものだけを圧縮する
def rle(xs, only):
    if not isinstance(only, set):
        only = {only}
    cur = None          # 今数えている文字。None なら数えていない
    res = []
    cnt = 0
    for i, v in enumerate(xs):
        if cur is None:
            if v in only:
                cnt += 1
                cur = v
                continue
            else:
                res.append((v, 1))
        else:
            if v == cur:
                cnt += 1
            else:
                res.append((cur, cnt))
                cnt = 0
                if v in only:          # 追加: 次も対象ならそのまま数え始める
                    cnt = 1
                    cur = v
                else:
                    res.append((v, 1))
                    cur = None
    if cur is not None:
        res.append((cur, cnt))
    return res
