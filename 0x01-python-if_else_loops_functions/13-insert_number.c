#include "lists.h"

/**
 * isert_node - insert a number into a sorted singly linked list
 * @head: pointer to the linked list head
 * @number: the number to be inserted
 * Return: a pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *node = malloc(sizeof(listint_t));
	
	if (!node)
		return (NULL);
	node->n = number;
	if (*head == NULL || number < ((*head)->n))
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	while(current->next && number > current->next->n)
		current = current->next;
	node->next = current->next;
	current->next = node;
	return(node);
}
