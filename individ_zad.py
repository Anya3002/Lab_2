#usr/bin/env python3
# -*- coding: utf-8 -*-
#Определить результат выполнения операций над множествами: A={b,e,g,h,k,s}; B={c,g,p,q}; C={f,g,s,x,y,z}; D={a,c,d,g,u,v,z}; X=(A+B)*C; Y=(An*D)+(C-B)

if __name__ == "__main__":

    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"b", "e", "g", "h", "k", "s"}
    b = {"c", "g", "p", "q"}
    c = {"f", "g", "s", "x", "y", "z"}
    d = {"a", "c", "d", "g", "u", "v", "z"}

    x = (a.union(b)).intersection(c)
    print(f"x = {x}")

    an = u.difference(a)

    y = (an.intersection(d)).union(c.difference(b))
    print(f"y = {y}")
