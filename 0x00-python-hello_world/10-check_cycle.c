#include "lists.h"

/**
 * check_cycle - function checks if linked list has cycles
 * @list: head node
 * Return: 0 if no, 1 if yes
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *head;

	if (list == NULL)
		return (0);

	current = list;
	head = list;

	while (current != NULL)
	{
		current = current->next;

		if (current == head)
		{
			return (1);
		}
	}

	return (0);
}
