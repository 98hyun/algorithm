#define _CRT_SECURE_NO_WARNINGS

#define TRUE	1
#define FALSE	0

#include <stdio.h>

typedef int Data;

typedef struct _node {
	Data data;
	struct _node* next;
} Node;

typedef struct _CLL {
	Node* tail;
	Node* cur;
	Node* before;
	int numOfData;
} CList;

typedef CList List;

void ListInit(List* plist);
void LInsert(List* plist, Data data);

int LFirst(List* plist, Data* pdata);
int LNext(List* plist, Data* pdata);
Data LRemove(List* plist);

void Delete(List* list, int target);
int NodeSearch(List* list, int k);

int main() {
	List list;
	ListInit(&list);
	int n, k;
	scanf("%d %d", &n, &k);

	for (int i = 1; i <= n; i++) {
		LInsert(&list, i);
	}
	NodeSearch(&list, k);
	return 0;
}

int NodeSearch(List* list, int k) {
	Node* start = list->tail->next;	
	printf("<");
	while (list->tail->next != list->tail) {
		for (int i = 1; i < k; i++) {
			start = start->next;
		}
		int target = start->data;
		printf("%d, ", target);
		start = start->next;

		Delete(list, target);
	}

	printf("%d>", list->tail->data);
	return 0;
}

void ListInit(List* plist) {
	plist->tail = NULL;
	plist->cur = NULL;
	plist->before = NULL;
	plist->numOfData = 0;
}

void LInsert(List* plist, Data data) {
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	if (plist->tail == NULL) {
		plist->tail = newNode;
		newNode->next = newNode;
	}
	else {
		newNode->next = plist->tail->next;
		plist->tail->next = newNode;
		plist->tail = newNode;
	}
	(plist->numOfData)++;
}

int LFirst(List* plist, Data* pdata) {
	if (plist->tail == NULL)
		return FALSE;

	plist->before = plist->tail;
	plist->cur = plist->tail->next;

	*pdata = plist->cur->data;
	return TRUE;
}

int LNext(List* plist, Data* pdata) {
	if (plist->tail == NULL) 
		return FALSE;

	plist->before = plist->cur;
	plist->cur = plist->cur->next;

	*pdata = plist->cur->data;
	return TRUE;
}

Data LRemove(List* plist) {
	Node* rpos = plist->cur;
	Data rdata = rpos->data;

	if (rpos == plist->tail) {
		if (plist->tail == plist->tail->next)   
			plist->tail = NULL;
		else
			plist->tail = plist->before;
	}

	plist->before->next = plist->cur->next;
	plist->cur = plist->before;

	free(rpos);
	(plist->numOfData)--;
	return rdata;
}

void Delete(List* list, int target) {
	int data;

	if (LFirst(list, &data))
	{
		if (data == target)
			LRemove(list);

		while (LNext(list, &data))
		{
			if (list->cur == list->tail) {
				if (data == target)
					LRemove(list);
				return;
			}
			if (data == target)
				LRemove(list);
		}
	}
}