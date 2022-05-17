#include <stdio.h>
#include <string.h>

#define BFLEN 13

/* 전역 변수 */
char cursorLeftKey = '<', cursorRightKey = '>', backspaceKey = '-';
char _inputBuffer[BFLEN] = "";

/*/////////*/

/* 함수 */
void titleMarkPrint() {
    printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[ 코드 디코더 ]\n--Made by iDSLR--\n\n\n\n");
   
}

void arrAdd(char* chstr, const int index, const char addstr, const int chstr_len) {
    
    for (int count=0; count<chstr_len-index; count++) {  // addstr을 넣기 위해 넣을 자리 앞에 있는 모든 변수를 1칸 앞으로 옮긴다.
        chstr[chstr_len-count] = chstr[chstr_len-1-count];
    }
    
    chstr[index] = addstr;  // 원하는 위치에 넣을 문자 addstr을 넣는다.
    
}

void arrDel(char* chstr, const int index, const int chstr_len) {  // index : 0부터.
    for (int count=0; count<chstr_len-(index-1); count++) {
        chstr[index-1+count] = chstr[index+count];
    }
}

char decoder_resultBuffer[BFLEN] = "";
char* decoder(char* chstr, int chstr_len) {
    
    int cursorIndex = 0;
    
    for (int count=0; count<chstr_len; count++) {
        if (chstr[count] == cursorLeftKey) {
             cursorIndex <= 0 ? NULL : cursorIndex--;
        } else if (chstr[count] == cursorRightKey) {
            cursorIndex >= strlen(decoder_resultBuffer) ? NULL : cursorIndex++;
        } else if (chstr[count] == backspaceKey) {
            arrDel(decoder_resultBuffer, cursorIndex, strlen(decoder_resultBuffer));
            cursorIndex--;
        } else {
            arrAdd(decoder_resultBuffer, cursorIndex, chstr[count], strlen(decoder_resultBuffer));
            cursorIndex++;
        }
    }
    
    //printf("\nlast cursorIndex = %d\n", cursorIndex);
    return decoder_resultBuffer;
    
}

/*/////*/

int main(int argc, char *argv[]) {
    char CLIprintMode = 1;  // 0 = 프로그램 종료, 1 = 코드 입력, 2 = 디코드된 결과 출력
    
    while (1) {
        for (int index=0; index<sizeof(decoder_resultBuffer)/sizeof(char); index++)
            decoder_resultBuffer[index] = NULL;
        
        if (CLIprintMode == 0) {
            return 0;
        } else if (CLIprintMode == 1) {
            titleMarkPrint();
            printf("\nCode = ");
            scanf("%s", _inputBuffer);
            
            CLIprintMode = 2;  // 디코드 결과 값 출력 상태로 전환.
        } else if (CLIprintMode == 2) {
            titleMarkPrint();
            printf("\nDecode result = \"%s\"", decoder(_inputBuffer, strlen(_inputBuffer)));
            
            REQU:;
            char yesorno = 0;
            printf("\ntry? [y]es or [n]o\n");
            scanf(" %c", &yesorno);
            
            if (yesorno == 'y') CLIprintMode = 1;
            else if (yesorno == 'n') CLIprintMode = 0;
            else goto REQU;
            
        }
        
    }
    
    return 0;
}