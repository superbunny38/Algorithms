char str[123456] = "";
char chars[123456] = "";

insert(idx, val)
    int idx;
    char val;
{
    int i;
    for(i=12345; i>idx; i--)
        str[i] = str[i-1];
    str[idx] = val;
    return 1;
}

remove(idx)
    int idx;
{
    int i;
    for(i=idx; i<12345; i++) {
        str[i] = str[i+1];
    }
    return 1;
}

print()
{
    int ln = strlen(str);
    int i;
    for(i=0; i<ln; i++) {
        if(str[i] == 32) continue;
        putchar(str[i]);
    }
    putchar(10);
}

main()
{
    gets(chars);
    int i;
    int ln = strlen(chars);
    int ptr = 0;
    int len = 0;
    for(i=0; i<123450; i++) *(str+i) = ' ';
    for(i=0; i<ln; i++) {
        int chr = *(chars+i);
        if(chr == '-') {
            remove(--ptr);
            len--;
        } else if(chr == '>') {
            if(ptr < len) ptr++;
        } else if(chr == '<') {
            if(ptr) ptr--;
        } else {
            insert(ptr++, chr);
            len++;
        }
    }
    print();
    return 0;
}

