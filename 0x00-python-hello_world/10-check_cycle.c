#include "lists.h"

/**
 * check_cycle - check if the linked list has a cycle
 * @list: the list to be checked 
 * Return: 1 cycle, 0 no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr_s, *ptr_f;

	if (!list || !list->next)
		return (0);
	ptr_s = list;
	ptr_f = list;
	while (ptr_s && ptr_f->next)
	{
		ptr_s = ptr_s->next;
		ptr_f = ptr_f->next->next;
		if (ptr_s == ptr_f)
		{
			return (1);
		}
	}
	return (0);
}
