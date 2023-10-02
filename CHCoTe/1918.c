#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_SIZE 100

typedef struct stack{
    char arr[MAX_SIZE];
    int top;
}Stack;

void init(Stack *st);
int bool_Empty(Stack *st);
int bool_Full(Stack *st);
void push(Stack *st, char elem);
char pop(Stack *st);
char peek(Stack *st);
void print(Stack *prev, Stack *next);
int priority(char elem);
int compS(char op1, char op2);
void conv(char *str);


int main(){
    int N = 1;
    for(int i = 0; i < N; i++){
        char str[MAX_SIZE] = {};
        scanf("%s", str);
        conv(str);
    }
    return 0;
}

void init(Stack *st){
    st->top = -1;
}

int bool_Empty(Stack *st){
    if(st->top == -1) return 1;
    else return 0;
}

int bool_Full(Stack *st){
    if(st->top == MAX_SIZE) return 1;
    else return 0;
}

int priority(char elem){
    if(elem == '!' || elem == '1' || elem == '2') return 6;
    else if(elem == '*' || elem == '/') return 5;
    else if(elem == '+' || elem == '-') return 4;
    else if(elem == '>' || elem == '<') return 3;
    else if(elem == '&') return 2;
    else if(elem == '|') return 1;
    return 0;
}

int compS(char op1, char op2){
    if(priority(op1) >= priority(op2)) return 1;
    else return 0;
}

void conv(char *str){
    int len = strlen(str);
    Stack nowStack, tmpStack;
    init(&nowStack);
    init(&tmpStack);
    for(int i = 0; i <= len; i++){
        if(str[i] == '+' || str[i] == '-'){
            if(i == 0)
                str[i] = str[i] == '+' ? '1' : '2';
            else if(!(str[i - 1] >= 'A' && str[i - 1] <= 'Z') && str[i - 1] != ')')
                str[i] = str[i] == '+' ? '1' : '2';
        }

        if(str[i] >= 'A' && str[i] <= 'Z')
            push(&nowStack, str[i]);
        else if(str[i] == '('){
            push(&tmpStack, str[i]);
        }
        else if(str[i] == ')'){
            while(1){
                char operator;
                if(bool_Empty(&tmpStack)) break;
                operator = pop(&tmpStack);
                if(operator == '(') break;
                else if(operator == '1') push(&nowStack, '+');
                else if(operator == '2') push(&nowStack, '-');
                else push(&nowStack, operator);
            }
        }
        else if(str[i] == '&' || str[i] == '|'){
            while(!bool_Empty(&tmpStack) && compS(peek(&tmpStack), str[i]) > 0){
                char operator = pop(&tmpStack);
                if(operator == '1') push(&nowStack, '+');
                else if(operator == '2') push(&nowStack, '-');
                else push(&nowStack, operator);
            }
            push(&tmpStack, str[i]);
            push(&tmpStack, str[i]);
            i += 1;
        }
        else{
            while(!bool_Empty(&tmpStack) && compS(peek(&tmpStack), str[i]) > 0){
                char operator = pop(&tmpStack);
                if(operator == '1') push(&nowStack, '+');
                else if(operator == '2') push(&nowStack, '-');
                else push(&nowStack, operator);
            }
            push(&tmpStack, str[i]);
        }
    }
    print(&nowStack, &tmpStack);
}

void push(Stack *st, char elem){
    st->top += 1;
    st->arr[st->top] = elem;
}

char pop(Stack *st){
    char tmp = st->arr[st->top];
    st->top -= 1;
    return tmp;
}

char peek(Stack *st){
    return st->arr[st->top];
}

void print(Stack *prev, Stack *next){
    int idx = 0;
    for(int i = 0; i <= prev->top; i++)
        printf("%c", prev->arr[i]);
    printf("\n");
}
