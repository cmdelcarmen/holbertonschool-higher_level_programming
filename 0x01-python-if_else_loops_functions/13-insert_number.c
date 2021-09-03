#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = NULL, *temp = *head, *temp_before;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return NULL;

	if (head == NULL)
	{
		node->n = number;
		node->next = NULL;
		return node;
	}

	while (temp != NULL)
	{
		if (temp->n > number)
			break;

		temp_before = temp;
		temp = temp->next;
	}
	/*will break out of loop when temp->n == 98*/

	node->n = number;
	node->next = temp;
	temp_before->next = node;

	return node;
}
