#include "lists.h"

/**
 * dup_list - duplicate a linked list.
 * @head: addredd to the head of the list.
 * Return: a new linked list.
 */
listint_t *dup_list(listint_t *head)
{
	listint_t *new = NULL;

	while (head)
	{
		if (!add_nodeint_end(&new, head->n))
			return (NULL);
		head = head->next;
	}

	return (new);
}

/**
 * reverse_list - reverse a linked list.
 * @head: head of the linked list.
 * Return: void.
 */
void reverse_list(listint_t **head)
{
	listint_t *current, *prev, *next;

	if (!*head)
		return;

	prev = NULL;
	current = *head;
	next = *head;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * size_list - get the size of the list.
 * @head: head of the list.
 * Return: integer.
 */
size_t size_list(listint_t *head)
{
	size_t size = 0;

	while (head)
	{
		size++;
		head = head->next;
	}
	return (size);
}

/**
 * is_palindrome - check if a linked list is palindrom.
 * @head: heade of the linked list.
 * Return: return 1 if it is palindrom else 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *rev, *tmp;
	size_t i = 0;

	if (!*head)
		return (1);

	tmp = *head;

	rev = dup_list(*head);

	reverse_list(&rev);

	while (tmp && rev && i < (size_list(*head) / 2))
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
		i++;
	}

	free_listint(rev);
	return (1);
}
