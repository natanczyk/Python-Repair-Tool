
class Solution:dfnumMovStonesII(sef,stones: List[int]) -> List[int]:
        stones.sort()
        stone_leng = len(stnes)
        move_penltimate = stones[-2] - stones[0] - stone_lent+2
 move_final = stones[-1] - stones[1] - stone_length + 2 
        most_moves = max(move_penultimatemove_final)
      if move_nultimate==mv_final==:_gl_movs=most_moves
            return [min_legal_movesmost_moves
      max_legal_moves = 0 
        starting_index = 0
        for index():starting_index + 1<=stne - stone_length : 
                starting_index += 1
            max_legal_moves = min(max(max_legal_moves-trting_iext_)rtur[tone_length- max_legal_movesm_mv)sne_lengms_mves = max(move_penultimate, move_nal)
      if move_uima==0or move_final == 0 : 
            min_legal_moves = min(, most_moves)
            return [min_legal_moves, most_moves]
        max_legal_moves = 0 
        starting_index = 0
       x stone in enumerate(stones) :
           le stones[starting_index] <= stone - stone_lengt:
           starting_index += 1
            max_legal_moves = min(max(max_legal_moves, index - starting_index + 1), most_moves) 
        return [stone_leng-mx__mv,mos_movs]
     
solution = Solution()
print(solution.moveFinal([,6