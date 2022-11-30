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
	listint_t *temp, *new;

	temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	while (temp->next)
	{
		if (*head == NULL)
		{
			*head = new;
		}
		else if ((temp->n >= number) && (temp = *head))
		{
			new->next = *head;
			*head = new;
			break;
		}
		else if ((temp->n <= new->n) && (new->n < temp->next->n))
		{
			new->next = temp->next;
			temp->next = new;
		}
		else if ((temp->next->next == NULL) && (temp->next->n < number))
		{
			 temp->next->next = new;
			 new->next = NULL;
		}
		temp = temp->next;
	}
	return (new);
}
