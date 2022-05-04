#include <stdio.h>
#pragma warning(disable: 4996)


//함수도 안 쓰고
//동적할당도 안 써야함!!
//포인터도 안됨
//오직 1차원 배열만 사용 가능
int main() {

	char s1[13];
	char password[13];
	int p_last = -1;

	printf("명령어: ");
	scanf("%s", s1);
	//printf("received: %s\n\n", s1);
	int cursor_on = -1;
	int last_idx = 0;
	for (int i = 0; i < 13; i++) {
		if (s1[i] == NULL) {
			last_idx = i - 1;
		}
		
	}

	for (int i = 0; i < 13; i++) {
		if (s1[i] == NULL) {
			break;
		}
		//printf("currently: %c, i: %d  ", s1[i],i);
		if (p_last == -1) {
			//printf("저장된 data 없음\n");
			if (s1[i] == '<' | s1[i] == '<' | s1[i] == '-') {
				continue;
			}
			else {
				password[0] = s1[i];
				cursor_on = 0;
				p_last = 0;
				continue;
			}
		}
		if (s1[i] == '<') {
			if (cursor_on == -1) {
				cursor_on = -1;
			}
			else {
				cursor_on -= 1;
			}
		}//<
		else if (s1[i] == '>') {
			//printf("p_last: %d", p_last);
			if (cursor_on >= p_last) {
				{};
			}
			else {
				cursor_on += 1;
			}
		}//>
		else if (s1[i] == '-') {
			if (cursor_on == -1) {
				{};
			}
			else if(cursor_on >= p_last){
				password[cursor_on] = NULL;
				cursor_on -= 1;
				p_last -= 1;
			}//BPAC -> BPC -> BC -> Bbc
			else {
				
				char tmp[13];
				int tmp_idx = 0;
				for (int o = cursor_on; o < p_last; o++) {
					password[o] = password[o+1];
				}
				
				p_last -= 1;
				cursor_on -= 1;
			}
		}
		else {//숫자 혹은 문자
			//insert between

			char tmp[13];
			int tmp_idx = 0;
			for (int k = 0; k < p_last-cursor_on+1;k++) {

				tmp[k] = password[cursor_on+tmp_idx+1];
				tmp_idx += 1;

			}
			password[cursor_on+1] = s1[i];
			cursor_on += 1;
			p_last += 1;
			for (int j = 0; j < tmp_idx; j++) {
				if (tmp[j] == NULL) {
					break;
				}
				password[cursor_on + j+1] = tmp[j];
			}
		}
		
		//printf("updated password: %s\n cursor: %d, command: %c\n", password, cursor_on, s1[i]);
		//printf("---------------------------------------\n\n\n");
	}
	//printf("\n\n\n\n");
	for (int u = 0; u < p_last + 1; u++) {
		printf("%c",password[u]);
	}
	return 0;
}