#include "lists.h"
#include <stddef.h>
/**
 * reverse - reverses a list
 * @head: list to revorse
 * Return: reversed list
 */
listint_t *reverse(listint_t **head)
{
	listint_t *list = *head, *nxt, *prv = NULL;

	while (list)
	{
		nxt = list->next;
		list->next = prv;
		prv = list;
		list = nxt;
	}
	*head = prv;
	return (*head);

}
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: list to check
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *list, *rev;
	int l = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	list = *head;
	while (list)
	{
		list = list->next;
		l++;
	}
	if (l % 2 != 0)
		return (0);
	list = *head;
	for (i = 0; i < l / 2; i++)
		list = list->next;
	rev = reverse(&list);
	while (rev)
	{
		if (rev->n != list->n)
			return (0);
		rev = rev->next;
		list = list->next;
	}
	return (1);
}
