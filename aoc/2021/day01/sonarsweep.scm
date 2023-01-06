#| Reads input file |#
(define (read-file name)
  (let ((port (open-input-file name)))
    (let file ((x (read port)))
      (if (eof-object? x)
          (begin
            (close-input-port port)
            '())
          (cons x (file (read port)))))))

(define lines-read (read-file "infile.ss"))


#|Counts number of times the next element of the sequence increases from the
   previous |#
(define (count-increased sequence)

  (define (compare-elements rest-of-sequence count)
    (if (null? (cdr rest-of-sequence)) 
        count
        (compare-elements (cdr rest-of-sequence) (if (< (car rest-of-sequence)
                                                        (cadr rest-of-sequence))
                                                     (+ count 1)
                                                     count))))

  (compare-elements sequence 0))

#|Sum three and three elements, and gather elements in new list|#
(define (sum-windows sequence)
    (if (null? (cddr sequence))
        '()
        (cons (+ (car sequence) (cadr sequence) (caddr sequence))
              (sum-windows (cdr sequence)))))


#| Driver code |#
(count-increased lines-read)
(count-increased (sum-windows lines-read))
