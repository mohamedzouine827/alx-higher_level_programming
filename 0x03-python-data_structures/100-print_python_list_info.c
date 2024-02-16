#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>
/**
 * print_python_list_info - print the list of information
 * @p: the information that we want to print
 */

void print_python_list_info(PyObject *p)
{
	long int var = (((PyVarObject *)(p))->ob_size);
	PyListObject *my_alloc = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", var);
	printf("[*] Allocated = %ld\n", my_alloc->allocated);
	for (int i = 0; i < var; i++)
	{
		printf("Element %d: %s\n", i, (((my_alloc->ob_item[i]))->ob_type)->tp_name);
	};

}
