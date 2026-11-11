import sys,re,os
P=r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-1_split_chapters'
H=r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters'
def lines(d,f):
    return [l.rstrip('\n') for l in open(os.path.join(d,f),encoding='utf-8') if l.strip()]
def main():
    f=sys.argv[1]; a=int(sys.argv[2]) if len(sys.argv)>2 else 1; b=int(sys.argv[3]) if len(sys.argv)>3 else 10**9
    p=lines(P,f);h=lines(H,f)
    for i,(x,y) in enumerate(zip(p,h),1):
        if a<=i<=b:
            print(f'#{i}\nP: {x}\nH: {y}')
main()
