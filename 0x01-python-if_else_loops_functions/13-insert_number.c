#include <stdio.h>
#include "lists.h"
#include <stdlib.h>
#include <string.h>
/**
 *insert_node - inserts a new node at a specified position
 *@head: pointer to first node
 *@number:number to be inserted
 *Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	int count = 1;
	listint_t *temp, *new;

	temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	while (temp->next)
	{
		temp = temp->next;
		count++;
		if (count == 5)
		{
			new->next = temp->next;
			temp->next = new;
		}
	}
	return (new);
}
