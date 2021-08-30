var a,b,c,d,plus,t,n,q,k,wer,wew:longint;
    ch:array[1..5000]of char;
    s:array[1..100000]of string;
    ans:array[1..100000]of longint;
function fak(x:longint):longint;
begin
        if x=1 then fak:=1
        else fak:=x*(fak(x-1));
end;
function comb(n,r:longint):longint;
begin
        comb:=fak(n)div(fak(r)*(fak(n-r)));
end;
procedure cek;
var x,y,temp:longint;
      det:array[1..1000000]of boolean;
begin
        fillchar(det,wew,true);
        for x:=1 to wew-1 do begin
                if det[x]=true then begin
                temp:=1;
                for y:=x+1 to wew do begin
                    if s[x]=s[y] then begin
                        det[y]:=false;
                        inc(temp);
                   end;
                end;
                if temp>k then ans[wer]:=ans[wer]+comb(temp,k);
                if temp=k then inc(ans[wer]);
                end;
                det[x]:=false;
        end;
end;
begin
        readln(t);
        for a:=1 to 5 do begin
            wer:=0;
            plus:=0;
            fillchar(ch,5000,' ');
            readln(n,q);
            wew:=((n*n)+n)div 2;
            for b:=1 to n do read(ch[b]);
            for b:=1 to n do begin
                for c:=1 to n-(b-1) do begin
                    inc(plus);
                    for d:=c to c+b-1 do s[plus]:=s[plus]+ch[d];
                end;
            end;
            for b:=1 to q do begin
                inc(wer);
                readln(k);
                cek;
                if k=1 then inc(ans[wer]);
            end;
            for b:=1 to wer do writeln(ans[b]);
        end;
readln;
end.