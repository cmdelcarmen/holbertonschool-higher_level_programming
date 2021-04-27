#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - function checks if linked list has cycles
 * @list: head node
 * Return: 0 if no, 1 if yes
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	if (list == NULL)
		return (0);

	current = list;

	while (current != NULL && (current->next != NULL))
	{
		current = current->next;

		if (current == list)
		{
			return (1);
		}
	}

	return (0);
}
