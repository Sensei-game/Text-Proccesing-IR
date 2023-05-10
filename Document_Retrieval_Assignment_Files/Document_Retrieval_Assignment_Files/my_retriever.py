
class Retrieve:
    """\
    Finish MEEE!!!
    
    DOO IIIITTTT
    
    Your task is to complete the definition of the Retrieve class, so that the overall IR system
    performs retrieval based on the vector space model.
    
    Your code should allow alternative term weighting schemes (selected by the \-w" option) to be used,
    i.e. binary vs. term frequency vs.TFIDF.
    
    Evaluate your system’s performance over the CACM test collection under the various
    configurations that arise from the alternative choices for preprocessing and for term weighting.
    """
    
    """
    Implementation and Code Style (18 marks): 
        
    How many term weighting schemes were correctly implemented? 
    Is the code efficient (i.e. are results returned quickly)? 
    Have appropriate Python constructs been used?
    Is the code comprehensible and suitably commented?
    
    Report (12 marks): 
    Is the report a clear and accurate description of the implementation?
    Are system performance results for a full range of configurations presented and discussed? 
    Are sensible inferences drawn about the performance from these results?
    """
    
    """
    Notes and Comments:
        
    1. Study the code in IR engine.py, to understand how the code of the Retrieve class (that
    you must complete) is called from the main program. [X]

    2. Within the program, the retrieval index is stored as a two-level dictionary structure, i.e.
    which maps terms to doc-ids to counts. (You might use a modified copy of IR engine.py
    as a means to probe the data structure, to ensure that you understand this vital point.) [X]

    3. The queries are stored as a list of pairs of the form (query-id, preprocessed-text), e.g. with
    text such as [’parallel’,’languages’,’languages’,’for’,’parallel’,’computation’] for
    query 10 with no stemming or stoplisting, but when both are in use, it instead becomes
    [’parallel’,’languag’,’languag’,’parallel’,’comput’]. (Given such repeated terms, it
    makes sense, in your code, to convert this representation to a dictionary of term counts.)[x]

    4. Only documents containing at least one term from the query can achieve similarity scores
    above zero. [REMEMBER THIS!!]
    All other documents can be ignored.[Interesting]
    The inverted index records, for any term,
    the documents in which appears, so it can be used to identify the candidate documents for
    which to compute similarity scores, to determine the top ranked candidates for return.[x]
s
    5. The vector space model views documents as vectors of term
    weights, and computes similarity as the cosine of the angle
    between the vectors. [x]
    
    As a comparison between document and query vectors, 
    this is calculated as shown on the right.
    cos(~q; d~) = pPn i=1 Pn iq=1 i2pqiPdi n i=1 d2 i [x]
    
    However, when we compute scores to rank the candidate documents for a single query, the
    component qPn i=1 qi2 (for the size of the query vector) is constant across comparisons, and
    so can be dropped without affecting how candidates are ranked. [x]

    6. Although the vector space model envisages documents as vectors with values for every
    term of the collection, we don’t actually need to construct these (enormous) vectors. In
    practice, only terms with non-zero weights will contribute. 
    
    For example, in computing the
    product Pn i=1 qidi, we need only consider the terms that are present in the query; for all
    other terms qi is zero, and so also is qidi.(Very important)
    
    (HOWEVER, when we compute the size of
    document vectors, all terms with non-zero weights should be considered.)[x]

    7. Although you are asked to expand the code in my retriever.py, so that the for query
    method performs ranked retrieval, this does not mean that you should only add code to
    the definition of this method. As always, other methods can be added to perform coherent
    subtasks (and making your code more readable). This is illustrated by the definition (in
    my retriever.py) of a method that computes, from the index, the number of documents
    in the collection. Other examples of methods that might reasonably be added include:
    
    a. A method to precompute the inverse document frequency value of each term in the
    collection, again based just on the inverted index. Thus, the index maps each term to
    the documents that contain it, whose number determines its document frequency.

    b. A method to precompute the document vector size for each document in the collection.
    Note that this can be computed for all documents at the same time, in a single pass over
    the index. Where TF.IDF term weighting is used, the IDF values must be computed
    before the document vector sizes are calculated.
    """
    
    # Create new Retrieve object storing index and term weighting 
    # scheme. (You can extend this method, as required.)
    
    # Index is a 2-level dictionary
    def __init__(self, index, term_weighting):
        self.index = index
        self.term_weighting = term_weighting
        self.num_docs = self.compute_number_of_documents()
        
    def compute_number_of_documents(self):
        self.doc_ids = set()
        for term in self.index:
            self.doc_ids.update(self.index[term])
        return len(self.doc_ids)

    # Method performing retrieval for a single query (which is 
    # represented as a list of preprocessed terms). Returns list 
    # of doc ids for relevant docs (in rank order).
    def for_query(self, query):
        return list(range(1,11))

"""\
# documents.txt, which contains a collection of documents that 
# record publications in the CACM (Communications of the Association for Computing Machinery). 

#queries.txt contains a set of IR queries for use against this collection
#cacm gold std.txt is a ‘gold standard’ 

# These three files together constitute a standard test set, or benchmark, 
# that has been used for evaluating IR
# systems (although it is now rather dated, not least by being very small by modern standards)
"""
