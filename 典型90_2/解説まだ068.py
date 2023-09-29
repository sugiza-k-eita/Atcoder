# 問題文 長さ N の整数列 A=(A 1 ​ ,A 2 ​ ,…,A N ​ ) があります。 はじめ、あなたはこの整数列について何も知りません。 整数列 A に関する情報と質問（まとめてイベントと呼ぶ）が Q 個与えられます。最初から i 番目 (1≤i≤Q) のイベントは 4 つの整数の組 (T i ​ ,X i ​ ,Y i ​ ,V i ​ ) で表され、これは次のようなものです。 T i ​ =0 のとき、これは A X i ​ ​ +A Y i ​ ​ =V i ​ という情報が与えられることを意味します。ここでは、必ず X i ​ +1=Y i ​ です。 T i ​ =1 のとき、これは A X i ​ ​ =V i ​ と仮定したとき A Y i ​ ​ の値は何か？という質問を意味します。 より厳密には、 A X i ​ ​ =V i ​ と A X j ​ ​ +A Y j ​ ​ =V j ​ (1≤j<i,T j ​ =0) がすべて成り立つような長さ N の整数列 A において、 A Y i ​ ​ の値は何か？ という質問を表します。 イベントを順に処理し、それぞれの質問に答えてください。 ただし、質問の時点で答え A Y i ​ ​ が一通りに定まらないとき、代わりに Ambiguous と出力してください。

        
# 累積和を動的に計算するときは、BITを使う