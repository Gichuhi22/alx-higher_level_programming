#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
 * check_cycle - checks for presence of loop in linked list
 * @list: pouinter to head of list
 * Return: 1 if loop found 0 if no loop
 */

int check_cycle(listint_t *list)
{
	listint_t *temp, *curr;
	int x;

	curr = temp = list;

	while(temp && curr && curr->next)
	{
		temp = temp->next;
		curr = curr->next->next;
		if (temp == curr)
		{
			x = 1;
			break;
		}
		else
		{
			x = 0;
		}
	}
	return (x);
}
