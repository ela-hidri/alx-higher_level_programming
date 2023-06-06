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

	if (list == NULL || list->n >= number)
	{
		newlist->next = list;
		*head = newlist;
		return (newlist);
	}
	while (list && list->next && list->next->n < number)
	{
		list = list->next;
	}
	newlist->next = list->next;
	list->next = newlist;
	return (newlist);

}
