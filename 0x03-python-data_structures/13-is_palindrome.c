#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the start of the list
 * Return: 1 if palindrome and  0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t  *tmp, *rev = NULL, *mid = *head, *fast = *head;
	
	if (!head)
		return (1);
	while (fast && fast->next)
	{
		fast = fast->next->next;
		tmp = mid;
		mid = mid->next;
		tmp->next = rev;
		rev = tmp;
	}
	
	if (fast)
		mid = mid->next;
	while (rev && mid)
	{
		if (rev->n != mid->n)
			return (0);
		rev = rev->next;
		mid = mid->next;
	}
	return (1);
}
