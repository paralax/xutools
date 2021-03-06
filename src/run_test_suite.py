"""
copyright (c) 2010-2013, Gabriel A. Weaver, Department of Computer
Science at Dartmouth College. <gabriel.a.l.weaver@gmail.com>

This file is part of XUTools, Python Distribution.

This code is free software:  you can redistribute                
it and/or modify it under the terms of the GNU General Public                   
License as published by the Free Software Foundation, either version            
3 of the License, or (at your option) any later version.                        
                                                                                
XUTools is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
for more details.
                                                                                
You should have received a copy of the GNU General Public License               
along with this program.  If not, see http://www.gnu.org/licenses/
"""
import unittest
import xutools.test.corpus as test_corpus
import xutools.test.tools as test_tools

xugrepSuite = unittest.TestLoader().loadTestsFromTestCase( test_tools.TestXUGrep )
xuwcSuite = unittest.TestLoader().loadTestsFromTestCase( test_tools.TestXUWc )
tools_suite = [ xugrepSuite, xuwcSuite ]

corpusSuite = unittest.TestLoader().loadTestsFromTestCase( test_corpus.TestCorpus )
corpusElementSuite = unittest.TestLoader().loadTestsFromTestCase( test_corpus.TestCorpusElement )
corpus_suite = [ corpusElementSuite, corpusSuite ] 

alltests = unittest.TestSuite( corpus_suite + tools_suite )
unittest.TextTestRunner(verbosity=2).run(alltests)
