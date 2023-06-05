#include "lists.h"

/**
 * check_cycle - check if the linked list has a cycle
 * @list: the list to be checked 
 * Return: 1 cycle, 0 no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr_s, *ptr_f;

	if (head == NULL || head->next == NULL)
		return (0);
	ptr_s = list->next;
	ptr_f = list->next->next;
	while (ptr_f)
	{
		if (ptr_s == ptr_f)
		{
			ptr_s = head;
			while (ptr_s != ptr_f)
			{
				ptr_s = ptr_s->next;
				ptr_f = ptr_f->next;
			}
			return (ptr_s);
		}
		ptr_s = ptr_s->next;
		ptr_f = ptr_f->next->next;
	}
	return (NULL);
}
