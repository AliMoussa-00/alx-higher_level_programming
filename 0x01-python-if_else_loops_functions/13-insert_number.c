#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert a node while reserving the sorting
 * @head: pointer to the head of the list
 * @number: value of the node
 * Return: the address of the new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (!new || !head || !*head)
		return (NULL);

	new->n = number;

	if (current->n > number)
	{
		new->next = current;
		current = new;

		return (new);
	}

	while (current && current->next && current->next->n < number)
		current = current->next;
	new->next = current->next;
	current->next = new;

	return (new);
}
