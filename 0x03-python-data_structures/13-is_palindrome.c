#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the start of the list
 * Return: 1 if palindrome and  0 if not
 */

int is_palindrome(listint_t **head)
{
	int i = 0, j, k;
	listint_t  *node = *head, *start, *end;
	
	if (!head)
		return (1);
	while (node)
	{
		node = node->next;
		i++;
	}
	start = *head, end = *head;
	for (j = 0; j < i / 2 ; j++)
	{
		for (k = j; k < i - 1; k++)
			end = end->next;
		if (end->n != start->n)
			return (0);
		start = start->next;
		end = *head;
	}
	return (1);
}
