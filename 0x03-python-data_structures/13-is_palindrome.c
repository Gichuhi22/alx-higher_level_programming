#include"lists.h"
#include<stdio.h>
#include<stdlib.h>
/**
 *is_palindrome - checks if a linked list is a palindrome
 *@head: pointer to first node
 *Return: returns 1 if palindrome or 0 if not
 */
int is_palindrome(listint_t **head)
{
	int num_nodes = 0, i = 0, j, x;
	listint_t *temp, *curr;
	int *num_array;

	temp = curr = *head;
	if (*head == NULL)
		return (1);

	while (temp != NULL)
	{
		temp = temp->next;
		num_nodes++;
	}
	if (num_nodes == 1)
		return (1);
	num_array = malloc(sizeof(int) * (num_nodes + 1));
	if (!num_array)
	{
		free(num_array);
		exit(1);
	}
	while (curr != NULL)
	{
		num_array[i] = curr->n;
		curr = curr->next;
		i++;
	}
	for (j = 0, i = (num_nodes - 1); j < num_nodes / 2; j++, i--)
	{
		if (num_array[j] != num_array[i])
		{
			x = 0;
			break;
		}
		else
			x = 1;
	}
	free(num_array);
	return (x);
}
