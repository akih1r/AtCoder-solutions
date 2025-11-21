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

N, K = map(int,input().split())
S = list(input())
S = rle(S)

cnt = 0
for i, tpl in enumerate(S):
    k, v = tpl
    if k == "1":
        cnt += 1
    if cnt == K:
        K_idx = i
        break

if K_idx > 0:
    S[K_idx], S[K_idx-1] = S[K_idx-1], S[K_idx]
        
        
def un_rle(S_rle):
    result_blocks = []
    for k, v in S_rle:
        result_blocks.append(k * v)

    ans = "".join(result_blocks)
    return ans
print(un_rle(S))
ans = un_rle(S)[:N]

print(ans)
            
        
