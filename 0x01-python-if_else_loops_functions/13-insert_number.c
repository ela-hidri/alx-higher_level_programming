#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head of node
 * @number: number to add
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newlist, *list = *head;

	newlist = malloc(sizeof(listint_t));
	if (newlist == NULL)
		return (NULL);
	newlist->n = number;

	if (list == NULL && list->n >= number)
	{
		newlist->next = NULL;
		*head = newlist;
		return (newlist);
	}
	while (list->next != NULL)
	{
		if (list->next->n >= number)
		{
			newlist->next = list->next;
			list->next = newlist;
			break;
		}
		list = list->next;
	}
	return (newlist);

}
