(define (domain train-domain)

(:predicates (train ?t) (station ?s) (railway ?r)(isin ?x ?y)
             (conn ?x ?y) (free ?x) (at ?x ?y) (instation ?x)
             (passed ?x ?y)
)

(:action move
    :parameters (?t ?from ?y)
    :precondition (and (train ?t)(at ?t ?from)(not(at ?t ?y))(free ?y)(not(free ?from))
                  (conn ?from ?y)(railway ?from)(railway ?y)(not(instation ?t))(not(passed ?t ?y))
    )
    :effect (and
        (not(at ?t ?from))
        (at ?t ?y)
        (free ?from)
        (not(free ?y))
        (passed ?t ?from)
    )
)

(:action stop
    :parameters (?t ?from ?y)
    :precondition (and (train ?t)(at ?t ?from)(not(free ?from))
                  (isin ?from ?y)(railway ?from)(station ?y)(not(instation ?t))
    )
    :effect (and
        (at ?t ?y)
        (instation ?t)
    )
)

(:action ready_to_start
    :parameters (?t ?from ?y)
    :precondition (and (train ?t)(at ?t ?from)(at ?t ?y)
                  (isin ?y ?from)(station ?from)(railway ?y)(instation ?t)
    )
    :effect (and
        (not(at ?t ?from))
        (not(instation ?t))
    )
)

)