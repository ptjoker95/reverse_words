/*
 * reverse_words.cxx
 * 
 * Copyright 2014 ptjoker95 <ptjoker95@ptjoker95notebook>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */

#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char **argv)
{
	int N;
	string line;
	
	if( argc != 2 )
	{
		cout << "Error: Enter Files Name" << endl;
		return 1;
	}
	
	ifstream myfile( argv[1] );
	
	myfile >> N;
	cout << "N: " << N << endl;
		
	for( int i=0; i<N; i++ )
	{
		getline( myfile, line );
		cout << line << endl;
	}
	
	return 0;
}

