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
