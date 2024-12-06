# create a tuple that multiplies
def pal(big_t):
    st=0
    end=len(big_t)-1
    while big_t[st]<big_t[end]:
        print(st*st+1)
        st=st+1
        end=end-1
        return True
    return False
big_t=(67,-1,12,98,-17)