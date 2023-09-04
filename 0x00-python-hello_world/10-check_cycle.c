#include "lists.h"

/**
 * check_cycle - check if there is a cycle in the linked list
 * @list: the head of the linked list
 * Return: 0 if there is no cycle, else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	first = list;
	second = list;

	while (first && first->next)
	{
		first = first->next->next;
		second = second->next;

		if (second == first)
			return (1);
	}
	return (0);
}
